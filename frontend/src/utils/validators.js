import {required, minLength, email, maxLength, sameAs, alpha} from "@vuelidate/validators/dist/raw.esm";

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
        }
    },
    full_name: {
        required,
        alpha,
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
        let password2 = {
            sameAs: sameAs(formData.password)
        }
        return {
            email: this.email,
            password: this.password,
            password2: password2,
            full_name: this.full_name,
            phone: this.phone,
            description: this.description
        }
    }
}

const getValidator = {
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

export const messages = {
    email: [
        getValidator.required('Email'),
        getValidator.email()
    ],
    full_name: [
        getValidator.required('Full name'),
        getValidator.minLength('Full name', 'full_name'),
        getValidator.alpha('alpha')
    ],
    phone: [
        getValidator.required('Phone number'),
        getValidator.minLength('Phone number', 'phone')
    ],
    password: [
        getValidator.required('Password'),
        getValidator.minLength('Password', 'password')
    ],
    password2: [
        getValidator.sameAs('passwords')
    ],
    description: [
        getValidator.required('Description'),
        getValidator.maxLength('Description', 'description'),
        getValidator.minLength('Description', 'description')
    ]
}
