import {constants} from "@/utils/validation";

export const getValidator = {
    minLength: function (what, formField) {
        return {
            name: "minLength",
            message: `${what} must be at least ${constants.minLength[formField]} characters long`
        };
    },
    required: function (what) {
        return {
            name: "required",
            message: `${what} cannot be blank`
        };
    },
    email: function () {
        return {
            name: "email",
            message: "Enter a valid email"
        };
    },
    maxLength: function (what, formField) {
        return {
            name: "maxLength",
            message: `${what} must be at max ${constants.minLength[formField]}`
        };
    },
    alpha: function (what) {
        return {
            name: "alpha",
            message: `${what} must contain only letters`
        };
    },
    sameAs: function (what) {
        return {
            name: "sameAs",
            message: `Your ${what.toLowerCase()} did not match`
        };
    }
};

