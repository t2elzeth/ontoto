import {ref} from "vue";

export const getInputFieldValidationClasses = function (field) {
    return {
        valid: field.$dirty && !field.$invalid,
        invalid: field.$dirty && field.$invalid
    };
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

