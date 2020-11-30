<template>
  <Navbar />
  <Sidebar />
  <div class="main">
    <form @submit.prevent="signUp">
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr />

        <FormField
          :v$field="v$.email"
          placeholder="Enter email"
          label-text="Email"
          form-field="email"
        />
        <FormField
          :v$field="v$.full_name"
          placeholder="Enter full name"
          label-text="Full name"
          form-field="full_name"
        />
        <FormField
          :v$field="v$.phone"
          placeholder="Enter phone number"
          label-text="Phone number"
          form-field="phone"
        />
        <FormField
          :v$field="v$.password"
          placeholder="Enter password"
          label-text="Password"
          input-type="password"
          form-field="password"
        />
        <FormField
          :v$field="v$.password2"
          placeholder="Repeat your password"
          label-text="Repeat password"
          input-type="password"
          form-field="password2"
        />
        <FormField
          :v$field="v$.description"
          placeholder="Enter description"
          label-text="Description"
          form-field="description"
        />

        <button type="submit" class="register-btn">Sign Up</button>
        <p class="agreement">
          By creating an account you agree to our
          <a href="#">Terms & Privacy</a>.
        </p>
      </div>

      <div class="container signin">
        <p>Already have an account? <a href="#">Sign in</a>.</p>
      </div>
    </form>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import FormField from "@/components/FormField";

import {
  email,
  required,
  sameAs,
  maxLength,
  minLength,
  alpha
} from "@vuelidate/validators/dist/raw.esm";
import { useVuelidate } from "@vuelidate/core";

import { success, error } from "@/utils/notifications";
import { formData } from "@/utils/forms";
import {validators} from "@/utils/validators";

export default {
  name: "SignUp",
  components: {
    Navbar,
    Sidebar,
    FormField
  },
  setup() {
    const signUpFormData = formData.signUp;

    const rules = {
      email: {
        required,
        email
      },
      password: {
        required,
        minLength: minLength(validators.minLength.password)
      },
      password2: {
        sameAs: sameAs(signUpFormData.password)
      },
      full_name: {
        required,
        alpha,
        minLength: minLength(validators.minLength.full_name)
      },
      phone: {
        required,
        minLength: minLength(validators.minLength.phone)
      },
      description: {
        required,
        maxLength: maxLength(validators.maxLength.description),
        minLength: minLength(validators.minLength.description)
      }
    };

    const v$ = useVuelidate(rules, signUpFormData);

    // axios
    //   .post(urls.signUp, signUpFormData)
    //   .then(res => console.log(res.data))
    //   .catch(err => console.log(err));

    function signUp() {
      // Validate data
      v$.value.$touch();

      // If data is invalid
      if (v$.value.$invalid) {
        error("Your data is invalid");
        return;
      }

      success("Your account has been successfully created");
    }

    return {
      signUp,
      v$,
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
</style>
