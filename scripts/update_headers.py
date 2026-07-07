import os
import re
from pathlib import Path


def update_workflow_headers(target_directory: Path):
    """
    Scans the target directory for Python files and updates the metadata headers
    from false to true for griptape provision and template flags.
    """
    if not target_directory.exists():
        print(
            f"❌ Error: Calculated target directory does not exist:\n   '{target_directory.resolve()}'"
        )
        return

    print(f"🔍 Scanning directory: {target_directory.resolve()}")

    # Regex patterns to safely catch the flags even if spacing varies slightly
    provided_pattern = re.compile(
        r"(#\s*is_griptape_provided\s*=\s*)false", re.IGNORECASE
    )
    template_pattern = re.compile(r"(#\s*is_template\s*=\s*)false", re.IGNORECASE)

    updated_files_count = 0

    # Iterate through all Python files in the target templates directory
    for file_path in target_directory.glob("*.py"):
        try:
            content = file_path.read_text(encoding="utf-8")

            # Check and replace values
            modified_content = content
            if provided_pattern.search(modified_content):
                modified_content = provided_pattern.sub(r"\1true", modified_content)
            if template_pattern.search(modified_content):
                modified_content = template_pattern.sub(r"\1true", modified_content)

            # Only write back to the file if changes were actually made
            if modified_content != content:
                file_path.write_text(modified_content, encoding="utf-8")
                print(f"✅ Updated: {file_path.name}")
                updated_files_count += 1
            else:
                print(f"➖ Skipped (No matching 'false' flags found): {file_path.name}")

        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")

    print(f"\n🎉 Done! Successfully updated {updated_files_count} templates.")


if __name__ == "__main__":
    # Script is in root/scripts/
    script_location = Path(__file__).parent

    # Target is root/workflows/templates/ -> Go up one level, then into workflows/templates
    target_dir = script_location.parent / "workflows" / "templates"

    update_workflow_headers(target_dir)
