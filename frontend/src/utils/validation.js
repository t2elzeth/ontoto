import {required, minLength, email, maxLength, sameAs, alpha} from "@vuelidate/validators/dist/raw.esm";

import {getValidator} from "@/utils/validators";

export const constants = {
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

export const rules = {
    email: {
        email, required
    },
    password: {
        required,
        minLength: minLength(constants.minLength.password)
    },
    login() {
        return {
            email: this.email,
            password: this.password
        }
    },
    full_name: {
        required, alpha,
        minLength: minLength(constants.minLength.full_name)
    },
    phone: {
        required,
        minLength: minLength(constants.minLength.phone)
    },
    description: {
        required,
        maxLength: maxLength(constants.maxLength.description),
        minLength: minLength(constants.minLength.description)
    },
    signUp(formData) {
        return {
            email: this.email,
            password: this.password,
            password2: {sameAs: sameAs(formData.password)},
            full_name: this.full_name,
            phone: this.phone,
            description: this.description
        }
    }
}

export const messages = {
    email: [
        getValidator.required(),
        getValidator.email()
    ],
    full_name: [
        getValidator.required(),
        getValidator.minLength("full_name"),
        getValidator.alpha()
    ],
    phone: [
        getValidator.required(),
        getValidator.minLength("Phone number", "phone")
    ],
    password: [
        getValidator.required(),
        getValidator.minLength("Password", "password")
    ],
    password2: [
        getValidator.sameAs("passwords")
    ],
    description: [
        getValidator.required(),
        getValidator.maxLength("description"),
        getValidator.minLength("Description", "description")
    ]
}
