const tokenKey = "token";

export const auth = {
  getCredentials: function() {
    return {
      headers: {
        Authorization: `Token ${this.getToken()}`
      }
    };
  },
  setCredentials: data => localStorage.setItem(tokenKey, data["auth_token"]),
  isAuthenticated: () => localStorage.getItem(tokenKey) || false,
  getToken: () => localStorage.getItem(tokenKey),

  removeToken: () => localStorage.removeItem(tokenKey)
};
