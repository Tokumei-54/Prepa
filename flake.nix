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
        buildInputs = with pkgs; with python310Packages; with ocamlPackages; [
          # Python 3.12 and related packages
          python310  # Upgraded Python version

          #python3XXPackages.
          # Python libraries for data science, ML, and deep learning
          jupyterlab
          ipython
          ipykernel
          matplotlib
          numpy
          pandas
          scipy
          opencv


          # Deep learning frameworks
          tensorflow 
          #tensorflow-bin #bug in python 3.12
          # pytorch

          # JupyterLab extensions
          jupyterlab-lsp
          jupyterlab-git


          # OCaml and related tools
          ocaml           # OCaml compiler
          dune-release           # Build system for OCaml

          #ocamlPackages.
          utop            # Interactive toplevel for OCaml
          ocamlformat     # OCaml code formatter
          merlin  # Editor integration for OCaml (autocomplete)
          ocp-indent  # OCaml code indentation
          findlib   # OCaml library manager

          # Additional OCaml libraries
          core
          base
          ocaml-lsp

          # Optional opam if needed
          # opam


        ];
      };
    });
}