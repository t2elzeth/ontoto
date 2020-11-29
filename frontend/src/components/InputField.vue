<template>
  <input
    class="input-field"
    :type="type"
    :placeholder="placeholder"
    v-model="v$.$model"
    :class="getInputFieldValidationClasses(v$)"
    :id="id"
  />
</template>

<script>
import { getInputFieldValidationClasses } from "@/utils/forms";

export default {
  name: "InputField",
  props: {
    type: {
      type: String,
      default: "text"
    },
    placeholder: String,
    v$field: Object,
    id: String
  },
  setup(props) {
    return {
      getInputFieldValidationClasses,
      v$: props.v$field
    };
  }
};
</script>

<style scoped lang="scss">
$default-bg: #ddd;
$valid-bg: #46ff46;
$invalid-bg: red;

$border-width: 2px;

.input-field {
  width: 100%;
  padding: 15px;
  margin: 5px 0 0 0;
  display: inline-block;
  border: $border-width hidden $default-bg;
  background: #f1f1f1;
}

.input-field:focus {
  background-color: $default-bg;
  outline: none;
}

.input-field.invalid {
  border: $border-width dashed $invalid-bg;
}

.input-field.valid {
  border: $border-width solid $valid-bg;
  background: $valid-bg;
}
</style>
