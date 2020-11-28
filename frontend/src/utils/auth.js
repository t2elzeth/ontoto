const tokenKey = "token";

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

  removeToken: () => localStorage.removeItem(tokenKey)
};
