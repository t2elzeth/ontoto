export const getInputFieldValidationClasses = function(field) {
  return {
    valid: field.$dirty && !field.$invalid,
    invalid: field.$dirty && field.$invalid
  };
};

export const getFieldLabelProps = function(for_id, text, field) {
  return {
    for: for_id,
    text: text,
    field: field
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
