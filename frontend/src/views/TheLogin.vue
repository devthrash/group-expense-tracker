<template>
  <form>
    <div class="field">
      <label class="label">Email</label>
      <div class="control">
        <input class="input" type="text" placeholder="Email" v-model="email">
      </div>
    </div>
    <div class="field">
      <label class="label">Password</label>
      <div class="control">
        <input class="input" type="password" placeholder="Password" v-model="password">
      </div>
      <p class="help is-danger" v-show="errorMsg.length">{{ errorMsg }}</p>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" @click="login">Login</button>
      </div>
    </div>
  </form>
</template>

<script>
import axios from "./../utils/http"

export default {
  name: "TheLogin",

  data() {
    return {
      email: '',
      password: '',
      errorMsg: ''
    }
  },

  methods: {
    login(e) {
      e.preventDefault()
      this.errorMsg = ''

      const config = {
        method: 'post',
        url: 'api/auth',
        data: {
          email: this.email,
          password: this.password
        }
      }

      axios(config)
          .then((response) => {
            localStorage.setItem('token', response.data.result.token)

            this.$router.push('/')
          })
          .catch(() => {
            this.errorMsg = 'Invalid credentials'
          })
    }
  }
}
</script>

<style scoped>

</style>
