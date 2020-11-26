const urljoin = require("url-join");

const apiServer = "http://127.0.0.1:8001/";
const tokenKey = "token";

export const urls = {
  signUp: urljoin(apiServer, "api/auth/users"),
  login: urljoin(apiServer, "api/auth/token/login"),
  logout: urljoin(apiServer, "api/auth/token/logout"),
  whoAmI: urljoin(apiServer, "api/auth/users/me")
};

export const auth = {
  getCredentials: function() {
    return {
      headers: {
        Authorization: `Token ${this.getToken()}`
      }
    };
  },
  setCredentials: token => localStorage.setItem(tokenKey, token),
  isAuthenticated: () => this.getToken() || false,

  getToken: () => localStorage.getItem(tokenKey),

  removeToken: () => localStorage.removeItem(tokenKey),

  formData: {
    login: {
      email: "",
      password: ""
    },
    signUp: {
      email: "",
      full_name: "",
      phone: "",
      password: "",
      password2: "",
      description: ""
    }
  }
};
