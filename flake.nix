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
        buildInputs = with pkgs; ([
          python312  
        ]
        ++ with python312Packages; [
          # Python libraries for data science, ML, and deep learning
          jupyterlab
          ipython
          ipykernel
          matplotlib
          numpy
          pandas
          scipy

          # Deep learning frameworks
          tensorflow-bin  # Bug fix for Python 3.12

          # JupyterLab extensions
          jupyterlab-lsp
          jupyterlab-git
        ]
        ++ [
          ocaml      # OCaml compiler
          dune-release    # Build system for OCaml
        ]
        ++ with ocamlPackages; [
          # OCaml and related tools
          utop            # Interactive toplevel for OCaml
          ocamlformat     # OCaml code formatter
          merlin          # Editor integration for OCaml (autocomplete)
          ocp-indent      # OCaml code indentation
          findlib         # OCaml library manager

          # Additional OCaml libraries
          core
          base
          ocaml-lsp

          # Optional opam if needed
          # opam
        ];)
      };
    });
}
