import { ref } from "vue";

export const getInputFieldValidationClasses = function(field) {
  return {
    valid: field.$dirty && !field.$invalid,
    invalid: field.$dirty && field.$invalid
  };
};

export const validators = {
  minLength: {
    password: 8,
    phone: 8,
    full_name: 5,
    description: 50
  },
  maxLength: {
    description: 1200
  }
};

export const formData = {
  login: {
    email: ref(""),
    password: ref("")
  },
  signUp: {
    email: ref(""),
    full_name: ref(""),
    phone: ref(""),
    password: ref(""),
    password2: ref(""),
    description: ref("")
  }
};

export function getStates(formData) {
  let obj = {};
  for (let el in formData) {
    let key = el.toString();
    obj[key] = formData[key].data;
  }
  return ref(obj);
}

export const getValidator = {
  minLength: function(what, formField) {
    return {
      name: "minLength",
      message: `${what} must be at least 
      ${validators.minLength[formField]} characters long`
    };
  },
  required: function(what) {
    return {
      name: "required",
      message: `${what} cannot be blank`
    };
  },
  email: function() {
    return {
      name: "email",
      message: "Enter a valid email"
    };
  },
  maxLength: function(what, formField) {
    return {
      name: "maxLength",
      message: `${what} must be at max 
      ${validators.minLength[formField]}`
    };
  },
  alpha: function(what) {
    return {
      name: "alpha",
      message: `${what} must contain only letters`
    };
  },
  sameAs: function(what) {
    return {
      name: "sameAs",
      message: `Your ${what.toLowerCase()} did not match`
    };
  }
};
