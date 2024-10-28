{
  description = "Prepa";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs { inherit system; };
      pythonPackages = pkgs.python312Packages;
      ocamlPackages = pkgs.ocamlPackages;
    in {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          python312
          ocaml
          dune-release
        ] ++ with pythonPackages; [
          jupyterlab
          ipython
          ipykernel
          matplotlib
          numpy
          pandas
          scipy
          tensorflow-bin
          jupyterlab-lsp
          jupyterlab-git
        ] ++ with ocamlPackages; [
          utop
          ocamlformat
          merlin
          ocp-indent
          findlib
          core
          base
          ocaml-lsp
        ];
      };
    });
}
