import os
from pathlib import Path

def generate_infer_yaml_files(entry_names, output_root="/users/ljunyu/data/ljunyu/projects/few_shot_concept/code/PiT/configs/infer"):
    """
    For each data entry name, creates a directory `infer_<name>` and generates 4 YAML files inside.

    Args:
        entry_names (list of str): List of data entry names.
        output_root (str or Path): Root directory where infer_<name> folders will be created.
    """
    yaml_templates = [
        "0_1_6_7",
        "4_5_2_3",
        "0_5_2_7",
        "4_1_6_3"
    ]

    output_root = Path(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    for entry in entry_names:
        entry_dir = output_root / f"infer_{entry}"
        entry_dir.mkdir(exist_ok=True)

        for combo in yaml_templates:
            yaml_path = entry_dir / f"infer_{combo}.yaml"
            with open(yaml_path, "w") as f:
                f.write(f"""prior_path: models/Piece-it-Together/models/products_ckpt/prior.ckpt
prior_repo:
crops_dir: assets/{entry}/{combo}
output_dir: inference/{entry}/{combo}
""")
            print(f"Created: {yaml_path}")

# Example usage
if __name__ == "__main__":
    # "chair_09_299", "chair_110_299", "chair_03_475", "chair_2_v1", "chair_2_v2", "chair_2_v3", "chair_2_v4", "car_classic_hatchback", "car_gtr_formula", "car_gtr_formula_v2", "car_truck_gtr", "formula_03_04", "formula_v1", 
    entries = ["chair_09_299", "chair_110_299", "chair_03_475", "chair_2_v1", "chair_2_v2", "chair_2_v3", "chair_2_v4", "car_classic_hatchback", "car_gtr_formula", "car_gtr_formula_v2", "car_truck_gtr", "formula_03_04", "formula_v1"]  # Replace with your list
    generate_infer_yaml_files(entries)