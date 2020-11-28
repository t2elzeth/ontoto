const urljoin = require("url-join");

export const apiServer = "http://127.0.0.1:8001/";

export const urls = {
  signUp: urljoin(apiServer, "api/auth/users"),
  login: urljoin(apiServer, "api/auth/token/login"),
  logout: urljoin(apiServer, "api/auth/token/logout"),
  whoAmI: urljoin(apiServer, "api/auth/users/me")
};
