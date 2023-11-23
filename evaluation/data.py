import json
import os

base_simulation_url = os.path.abspath("../environment/frontend_server/storage")

def get_all_generate_data(simulation="base_the_ville_isabella_maria_klaus"):
    simulation_data_path = os.path.join(base_simulation_url, simulation)
    # assert not os.path.exists(simulation_data_path), f"该存档数据已存在于{simulation_data_path}"

    persons = []
    meta_path = os.path.join(simulation_data_path, "reverie", "meta.json")
    with open(meta_path, 'r', encoding='utf-8') as f:
        persons = json.load(f)['persona_names']

    datas = []
    for index, person_name in enumerate(persons):
        scratch = {}
        scratch_path = os.path.join(simulation_data_path, "personas",person_name, "bootstrap_memory", "scratch.json")
        with open(scratch_path, 'r') as f:
            scratch = json.load(f)
            daily_plan = scratch["daily_req"]
            hourly_schedule = [plan[0] for plan in scratch["f_daily_schedule_hourly_org"]]
            detail_plan = [plan[0] for plan in scratch["f_daily_schedule"]]
            detail_plan_cleaned = [plan[plan.find("(")+1:plan.find(")")] for plan in detail_plan if plan.find("(") != -1]

        node_path = os.path.join(simulation_data_path, "personas",person_name, "bootstrap_memory", "associative_memory", "nodes.json")
        with open(node_path, 'r') as f:
            nodes = json.load(f)
            conversation_node = [nodes[node] for node in nodes.keys() if nodes[node]['type'] == "chat"]  # 收集所有对话节点
            conversation = [conv[1] for conv_node in conversation_node for conv in conv_node['filling']]  # 收集节点中的对话
            thought = [nodes[node]['description'] for node in nodes.keys() if nodes[node]['type'] == "thought"]

        datas.append({
            "name":person_name,
            "daily_plan": daily_plan,
            "hourly_schedule" : hourly_schedule,
            "detail_plan":detail_plan_cleaned,
            "conversation":conversation,
            "thought":thought
        })
    return datas


if __name__ == "__main__":
    data = get_all_generate_data("25_February_13_2023_07_46_00")
    print(data[0].keys())
    print(data[2]['thought'])
    print(data[2]['name'])
