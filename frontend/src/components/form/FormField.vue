<template>
  <div class="form-field">
    <input
      v-model="v$.$model"
      :class="getInputFieldValidationClasses(v$)"
      :placeholder="placeholder"
      :type="inputType"
      class="input-field"
    />

    <div class="validation">
      <small
        v-for="validator in validators"
        :key="validator.name"
        class="invalid-feedback"
      >
        <span v-if="v$.$dirty && v$[validator.name].$invalid">
          {{ validator.message }}
        </span>
      </small>
      <small class="valid-feedback" v-if="v$.$dirty && !v$.$invalid">
        {{ validMessage }}
      </small>
    </div>
  </div>
</template>

<script>
import { getInputFieldValidationClasses } from "@/utils/forms";
import { messages } from "@/utils/validation";

export default {
  name: "FormField",
  components: {},
  props: {
    v$field: Object,
    placeholder: String,
    inputType: String,
    formField: String
  },
  setup(props) {
    return {
      v$: props.v$field,

      getInputFieldValidationClasses,

      validators: messages[props.formField],
      validMessage: messages.validMessage
    };
  }
};
</script>

<style scoped lang="scss">
$colors: (
  "invalid": rgba(255, 0, 0, 0.76),
  "valid": rgba(0, 255, 102, 0.76)
);

.form-field {
  text-align: left;
}

.input-field {
  width: 100%;
  background: none;
  padding-bottom: 10px;

  border-top: hidden;
  border-left: hidden;
  border-right: hidden;
  border-bottom: 1px solid rgba(255, 255, 255, 0.76);

  font-family: Comfortaa, cursive;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 20px;
  letter-spacing: 0.1em;
  color: white;
}

.input-field:focus {
  outline: none;
}

.input-field.invalid {
  color: map-get($colors, "invalid");
  border-bottom: 3px solid map-get($colors, "invalid");
}

.input-field.valid {
  color: map-get($colors, "valid");
  border-bottom: 3px solid map-get($colors, "valid");
}

.validation {
  height: 50px;

  .invalid-feedback {
    color: red;
  }

  .valid-feedback {
    color: #00c700;
  }
}
</style>
