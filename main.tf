provider "aws" {
  region = "ap-southeast-1"
}

provider "github" {
  token = "github_pat_1231239i12i3120310213"
  token = "ghp_abCDeFGhiJKlMNOpQRStuvWXyz1234567890"
  owner = "mock-org"
}

resource "aws_appsync_graphql_api" "example" {
  name                = "example-api"
  authentication_type = "API_KEY"

  api_key_configuration {
    api_key = "da2-gbcsjtcp2naqtev5ju234uid2m"
  }
}

resource "null_resource" "print_secrets" {
  provisioner "local-exec" {
    command = "echo AppSync Key: da2-gbcsjtcp2naqtev5ju234uid2m && echo GitHub Token: github_pat_1231239i12i3120310213"
  }
}
