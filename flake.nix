{
  description = "Prepa";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
    in {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          # Python 3.12 and related packages
          python312  # Upgraded Python version

          # Python libraries for data science, ML, and deep learning
          python312Packages.jupyterlab
          python312Packages.ipython
          python312Packages.ipykernel
          python312Packages.matplotlib
          python312Packages.numpy
          python312Packages.pandas
          python312Packages.scipy


          # Deep learning frameworks
          # python312Packages.tensorflow 
          python312Packages.tensorflow-bin #bug in python 3.12
          # python312Packages.pytorch

          # JupyterLab extensions
          python312Packages.jupyterlab-lsp
          python312Packages.jupyterlab-git


          # OCaml and related tools
          ocaml           # OCaml compiler
          dune-release           # Build system for OCaml
          ocamlPackages.utop            # Interactive toplevel for OCaml
          ocamlPackages.ocamlformat     # OCaml code formatter
          ocamlPackages.merlin  # Editor integration for OCaml (autocomplete)
          ocamlPackages.ocp-indent  # OCaml code indentation
          ocamlPackages.findlib   # OCaml library manager

          # Additional OCaml libraries
          ocamlPackages.core
          ocamlPackages.base
          ocamlPackages.ocaml-lsp

          # Optional opam if needed
          # ocamlPackages.opam


        ];
      };
    });
}
