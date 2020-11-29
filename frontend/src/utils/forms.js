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
    fullname: 5,
    description: 50
  },
  maxLength: {
    description: 1200
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
