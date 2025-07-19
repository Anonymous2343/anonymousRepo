import json

def extract_task_info(source_file):
    """
    Extracts the optimization type and task ID from the source_file path
    using string manipulation only.
    """
    filename = source_file.split('/')[-1]  # Get the file name from the path
    parts = filename.split('_')  # Example: ["O0", "source", "53.c"]
    if len(parts) >= 3 and parts[-2] == "source":
        optimization = parts[0]
        task_id_str = parts[-1].replace(".c", "")
        try:
            task_id = int(task_id_str)
            return task_id, optimization
        except ValueError:
            return None, None
    return None, None

def load_eval_results(file_path):
    """
    Loads eval_results.jsonl into a dictionary indexed by (task_id, type).
    """
    eval_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            entry = json.loads(line)
            key = (entry["task_id"], entry["type"])
            eval_dict[key] = (entry["compile_passed"], entry["test_passed"])
    return eval_dict

def process_files(functions_log_path, eval_results_path, output_path):
    eval_results = load_eval_results(eval_results_path)

    with open(functions_log_path, 'r') as f_in, open(output_path, 'w') as f_out:
        for line in f_in:
            func_entry = json.loads(line)
            task_id, opt = extract_task_info(func_entry["source_file"])
            if task_id is None or opt is None:
                continue

            eval_key = (task_id, opt)
            if eval_key in eval_results:
                compile_passed, test_passed = eval_results[eval_key]
                func_compilable = func_entry.get("compilable", 0)
                func_pass = func_entry.get("pass", 0)
                f_out.write(f"{compile_passed} {test_passed} {func_compilable} {func_pass}\n")

if __name__ == "__main__":
    functions_log_path = "function_logs.jsonl"
    eval_results_path = "eval_results.jsonl"
    output_path = "comparison_output.txt"
    process_files(functions_log_path, eval_results_path, output_path)
