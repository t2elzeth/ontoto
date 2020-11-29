<template>
  <div class="form-field">
    <FieldLabel :for="id" :text="labelText" :v$field="v$" />
    <InputField
      :type="inputType"
      :placeholder="placeholder"
      :v$field="v$"
      :id="id"
    />

    <ValidationMessages :v$field="v$" :validators="validators" />
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
    id: String,
    placeholder: String,
    labelText: String,
    validators: Array,
    inputType: String
  },
  setup(props) {
    return {
      v$: props.v$field
    };
  }
};
</script>

<style scoped></style>
