# Contributing to Griptape Nodes X Nuke Workflows

We welcome contributions to the Griptape Nodes X Nuke Workflows library! This library provides Nuke-specific workflow nodes for Griptape Nodes.

## Development Setup

1. **Clone the Repository:**

    ```shell
    git clone <repo-url>
    cd griptape-nodes-x-nuke-workflows
    ```

1. **Install `uv`:**
    If you don't have `uv` installed, follow the official instructions: [Astral's uv Installation Guide](https://docs.astral.sh/uv/getting-started/installation/).

1. **Install Dependencies:**
    Use `uv` to create a virtual environment and install all required dependencies:

    ```shell
    uv sync --all-groups --all-extras
    ```

    Or use the Makefile shortcut:

    ```shell
    make install
    ```

## Contributing Code

1. **Find the library code** - All workflow nodes for this library are located in:

    ```
    griptape_nodes_x_nuke_workflows/workflows/
    ```

    Current workflows:

    - `nuke_upscale_workflow.py` - SeedVR image upscaling workflow
    - `nuke_flux_inpainting.py` - Flux-based inpainting workflow
    - `nuke_OpenPose_Video_Detection.py` - OpenPose video detection workflow
    - `nuke_WAN_Reference_to_Video.py` - WAN reference-to-video generation workflow

1. **Make your changes** - Follow the existing code structure and style in the library.

1. **Run tests** - Test the library to ensure your changes work:

    ```shell
    make test
    ```

    Or run a specific test suite:

    ```shell
    make test/unit
    make test/workflows
    ```

1. **Follow code quality standards** - Run checks before submitting:

    ```shell
    make check  # Check linting, formatting, and type errors
    make fix    # Auto-fix issues where possible
    ```

1. **Submit a pull request** - Open a PR against the `main` branch of this repository.

## Making a Release (Maintainers)

The library version is stored in `griptape_nodes_x_nuke_workflows.json` under the `metadata.library_version` field. Releases involve bumping the version and publishing tags.

### Step 1: Bump the Version

```shell
make version/patch   # Bump patch (e.g. 0.1.0 -> 0.1.1)
make version/minor   # Bump minor (e.g. 0.1.1 -> 0.2.0)
make version/major   # Bump major (e.g. 0.2.0 -> 1.0.0)
```

These targets update `griptape_nodes_x_nuke_workflows.json`, commit the change, and you can then `git push`.

### Step 2: Publish the Release

```shell
make version/publish
```

## Questions or Issues?

For questions about contributing, please open an issue in this repository.

Thank you for contributing!
