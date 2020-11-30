<template>
  <div class="form-field">
    <FieldLabel :for="id" :text="labelText" :v$field="v$" />
    <InputField
      :type="inputType"
      :placeholder="placeholder"
      :v$field="v$"
      :id="id"
    />

    <ValidationMessages :v$field="v$" :field-name="formField" />
  </div>
</template>

<script>
import FieldLabel from "@/components/FieldLabel";
import InputField from "@/components/InputField";
import ValidationMessages from "@/components/ValidationMessages";

export default {
  name: "FormField",
  components: {
    FieldLabel,
    InputField,
    ValidationMessages
  },
  props: {
    v$field: Object,
    placeholder: String,
    labelText: String,
    inputType: String,
    formField: String,
  },
  setup(props) {
    return {
      v$: props.v$field,
      id: props.fieldName
    };
  }
};
</script>

<style scoped></style>
