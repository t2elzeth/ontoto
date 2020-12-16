import { constants } from "@/utils/validation";

export const getValidator = {
  minLength: function(formField) {
    return {
      name: "minLength",
      message: `Это поле должно быть как минимум ${constants.minLength[formField]} символов в длину`
    };
  },

  required: function() {
    return {
      name: "required",
      message: "Это поле не может быть пустым"
    };
  },
  email: function() {
    return {
      name: "email",
      message: "Введите валидный email адрес"
    };
  },
  maxLength: function(formField) {
    return {
      name: "maxLength",
      message: `Это поле не может превышать ${constants.minLength[formField]} символов в длину`
    };
  },
  alpha: function() {
    return {
      name: "alpha",
      message: "Это поле должно содержать только буквы"
    };
  },
  sameAs: function(what) {
    return {
      name: "sameAs",
      message: `Ваши ${what.toLowerCase()} не совпали`
    };
  }
};
