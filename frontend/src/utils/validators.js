import {constants} from "@/utils/validation";

export const getValidator = {
    minLength: function (formField) {
        return {
            name: "minLength",
            message: `This field must be at least ${constants.minLength[formField]} characters long`
        };
    },
    required: function () {
        return {
            name: "required",
            message: "This field cannot be blank"
        };
    },
    email: function () {
        return {
            name: "email",
            message: "Enter a valid email"
        };
    },
    maxLength: function (formField) {
        return {
            name: "maxLength",
            message: `This field must be at max ${constants.minLength[formField]}`
        };
    },
    alpha: function () {
        return {
            name: "alpha",
            message: "This field must contain only letters"
        };
    },
    sameAs: function (what) {
        return {
            name: "sameAs",
            message: `Your ${what.toLowerCase()} did not match`
        };
    }
};

