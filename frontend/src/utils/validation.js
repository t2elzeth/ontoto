import {
  required,
  minLength,
  email,
  sameAs
} from "@vuelidate/validators/dist/raw.esm";

import { getValidator } from "@/utils/validators";

export const constants = {
  minLength: {
    username: 8,
    password: 8
  }
};

export const rules = {
  username: {
    required,
    minLength: minLength(constants.minLength.username)
  },
  email: {
    email,
    required
  },
  password: {
    required,
    minLength: minLength(constants.minLength.password)
  },
  login() {
    return {
      email: this.email,
      password: this.password
    };
  },
  signUp(formData) {
    return {
      username: this.username,
      email: this.email,
      password: this.password,
      password2: { sameAs: sameAs(formData.password) }
    };
  }
};

export const messages = {
  validMessage: "все правильно!",

  username: [getValidator.required(), getValidator.minLength("username")],
  email: [getValidator.required(), getValidator.email()],
  password: [getValidator.required(), getValidator.minLength("password")],
  password2: [getValidator.sameAs("пароли")]
};
