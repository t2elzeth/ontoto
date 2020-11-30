
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

export const getValidator = {
    minLength: function (what, formField) {
        return {
            name: "minLength",
            message: `${what} must be at least 
      ${validators.minLength[formField]} characters long`
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
            message: `${what} must be at max 
      ${validators.minLength[formField]}`
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
