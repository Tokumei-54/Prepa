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
        buildInputs = with pkgs; with ocamlPackages; [
          # Python environment with selected packages
          (python3.withPackages (python-pkgs: with python-pkgs; [
            jupyterlab
            jupyter
            ipython
            ipykernel
            matplotlib
            pyqt5
            numpy
            pandas
            scipy
            opencv
            pyserial
            # tensorflow
          ]))

          # Full Qt environment
          qt5Full

          # OCaml environment and tools
          ocaml           # OCaml compiler
          opam
          dune-release     # Build system for OCaml
          utop            # Interactive toplevel for OCaml
          ocamlformat     # OCaml code formatter
          merlin           # Editor integration for OCaml
          ocp-indent       # OCaml code indentation
          findlib          # OCaml library manager
          ocaml-lsp        # Language server for OCaml
        ];
      };
    });
}
