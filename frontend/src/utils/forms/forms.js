import { ref } from "vue";

const getRef = (content = "") => ref(content);

const getFormData = (...fields) => {
  let formData = {};

  fields.forEach(field => {
    if (typeof field === "string") formData[field] = getRef();
    else formData[field[0]] = getRef(field[1]);
  });
  return formData;
};

export const formData = {
  login: getFormData("email", "password"),
  signUp: getFormData("username", "email", "password", "password2")
};
