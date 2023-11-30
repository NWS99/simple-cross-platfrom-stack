{ pkgs ? import <nixpkgs> {} }:
  let
    needed-packages = ps: with ps; [
      flet
      fastapi
      pydantic

# TODO: find all needed dependencies in fastapi-sqlalchemy and include them

#      (
#        buildPythonPackage rec {
#          pname = "fastapi-sqlalchemy";
#          version = "0.2.1";
#          src = fetchPypi {
#            inherit pname version;
#            sha256 = "sha256-0aozmQ4Eb5zL4rtNHSFjEynfObUkYlid1PgMDVmRkwY=";
#          };
#          doCheck = false;
#          propagatedBuildInputs = [
#            pkgs.python3Packages.sqlalchemy
#          ];
#        }
#      )
    ];
  in

  pkgs.mkShell {
    packages = with pkgs;
    [
      docker
      (python310.withPackages needed-packages)
      python310Packages.pip
      python310Packages.virtualenv
    ];
}
