import os
import shutil
from pathlib import Path

def copy_mask_cutouts(ref_data_root, target_data_root, entry_names):
    """
    Copies specified mask cutout images from reference data root to structured folders in target data root.

    Args:
        ref_data_root (str or Path): Path to the reference data root.
        target_data_root (str or Path): Path to the output data root.
        entry_names (list of str): List of data entry folder names to process.
    """
    # Define folder names and their corresponding index mappings
    folder_map = {
        "0_1_6_7": [0, 1, 2, 3],
        "4_5_2_3": [0, 1, 2, 3],
        "0_5_2_7": [0, 1, 2, 3],
        "4_1_6_3": [0, 1, 2, 3],
    }
    index_map = {
        "0_1_6_7": [(0, 0), (0, 1), (1, 2), (1, 3)],
        "4_5_2_3": [(1, 0), (1, 1), (0, 2), (0, 3)],
        "0_5_2_7": [(0, 0), (1, 1), (0, 2), (1, 3)],
        "4_1_6_3": [(1, 0), (0, 1), (1, 2), (0, 3)],
    }

    for entry in entry_names:
        ref_entry_path = Path(ref_data_root) / entry
        target_entry_path = Path(target_data_root) / entry
        target_entry_path.mkdir(parents=True, exist_ok=True)

        # Get subfolders (assuming 2 subfolders in order)
        subfolders = sorted([d for d in ref_entry_path.iterdir() if d.is_dir()])
        assert len(subfolders) == 2, f"{entry} does not contain exactly 2 subfolders."

        for folder_name, indices in index_map.items():
            dest_folder = target_entry_path / folder_name
            dest_folder.mkdir(exist_ok=True)

            for i, (subfolder_idx, mask_idx) in enumerate(indices):
                src_file = subfolders[subfolder_idx] / f"mask{mask_idx}_cutout.png"
                dst_file = dest_folder / f"mask{i}_cutout.png"
                shutil.copy(src_file, dst_file)
                print(f"Copied {src_file} → {dst_file}")

# Example usage
if __name__ == "__main__":
    ref_data_root = "/users/ljunyu/data/ljunyu/projects/few_shot_concept/code/break-a-scene/examples_vis"
    target_data_root = "/users/ljunyu/data/ljunyu/projects/few_shot_concept/code/PiT/assets"
    entry_names = ["chair_09_299", "chair_110_299", "chair_03_475", "chair_2_v1", "chair_2_v2", "chair_2_v3", "chair_2_v4", "car_classic_hatchback", "car_gtr_formula", "car_gtr_formula_v2", "car_truck_gtr", "formula_03_04", "formula_v1", "creature_pit_v1_coarse", "creature_pit_v2_coarse"]
    copy_mask_cutouts(ref_data_root, target_data_root, entry_names)