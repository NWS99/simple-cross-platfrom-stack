{ pkgs ? import <nixpkgs> {} }:
let
  python-packages = ps: with ps; [
    flet
    fastapi
    pydantic
    psycopg2
    sqlalchemy
    uvicorn
    buildPythonPackage rec {
      pname = "fastapi-crudrouter";
      version = "v0.8.6";
      src = fetchPypi {
        inherit pname version;
        sha256 = "sha256-0aozmQ4Eb5zL4rtNHSFjEynfObUkYlid1PgMDVmRkwY=";
      };
      doCheck = false;
    }
  ];
in
  
pkgs.mkShell {
  nativeBuildInputs = with pkgs.buildPackages; 
    [
      docker
      docker-compose
      (python310.withPackages python-packages)
    ];
}
