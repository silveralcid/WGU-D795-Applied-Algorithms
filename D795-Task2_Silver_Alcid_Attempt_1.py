# Dijkstra’s Algorithm

import pandas as pd
import networkx as nx
import time
import os

# Load CSVs
ambulances_df = pd.read_csv("ambulance.csv")
calls_df = pd.read_csv("calls.csv")
call_priority_df = pd.read_csv("call_priority.csv")
location_network_df = pd.read_csv("location_network.csv")

# ambulance Number' as 'Ambulance ID' and assume delay time = 0
ambulances_df = ambulances_df.rename(
    columns={"Ambulance Number": "Ambulance ID"})
ambulances_df["Delay Time"] = 0.0

calls_df = calls_df.rename(columns={"Location": "Call Location"})

# "Time Received" for arrival
calls_df["Time Received"] = range(len(calls_df))

# Merge priority info and sort
calls_df = calls_df.merge(call_priority_df, on="Call Type")
calls_df = calls_df.sort_values(by=["Priority", "Time Received"])

# Build Graph
G = nx.DiGraph()
for _, row in location_network_df.iterrows():
    G.add_edge(row["Start"], row["End"], weight=row["Travel Time"])

# run dispatch sim
log_entries = []
total_route_time = 0.0

for _, call in calls_df.iterrows():
    call_location = call["Call Location"]
    call_id = call["Call ID"]
    call_type = call["Call Type"]

    best_ambulance = None
    best_time = float("inf")
    best_path = None

    for _, amb in ambulances_df.iterrows():
        staging_location = amb["Staging Location"]
        delay = amb["Delay Time"]

        try:
            start_time = time.time()
            path = nx.dijkstra_path(
                G, staging_location, call_location, weight="weight")
            path_time = nx.dijkstra_path_length(
                G, staging_location, call_location, weight="weight")
            end_time = time.time()

            total_time = path_time + delay
            total_route_time += (end_time - start_time)

            if total_time < best_time:
                best_time = total_time
                best_ambulance = amb["Ambulance ID"]
                best_path = path
        except nx.NetworkXNoPath:
            continue

    if best_ambulance is not None:
        log_entries.append({
            "Call ID": call_id,
            "Call Type": call_type,
            "Call Location": call_location,
            "Selected Ambulance": best_ambulance,
            "Route to Call Location": "->".join(best_path),
            "Time to the Call Location": best_time
        })

# write log and print
log_file = "ambulance_call_log.csv"
log_df = pd.DataFrame(log_entries)
log_df.to_csv(log_file, index=False)

print(
    f"Total Execution Time (Fastest Route Calculations): {total_route_time:.4f} seconds")
