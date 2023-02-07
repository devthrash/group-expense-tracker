<template>
  <form>
    <div class="field">
      <label class="label">Name</label>
      <div class="control">
        <input class="input" type="text" placeholder="Name" v-model="name">
      </div>
    </div>
    <div class="field">
      <label class="label">Members</label>
      <div class="control">
        <textarea class="textarea" placeholder="Members" v-model="members"></textarea>
      </div>
      <p class="help is-danger" v-show="errorMsg.length">{{ errorMsg }}</p>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" @click="createGroup">Create</button>
      </div>
    </div>
  </form>
</template>

<script>
import axios from "../utils/http";

export default {
  name: "NewGroup",

  data() {
    return {
      name: '',
      members: '',
      errorMsg: ''
    }
  },

  methods: {
    createGroup(e) {
      e.preventDefault()
      this.errorMsg = ''

      const config = {
        method: 'post',
        url: 'api/groups',
        data: {
          name: this.name,
          members: this.members.split('\n')
        }
      }

      axios(config)
          .then((response) => {
            this.$router.push('/group/' + response.data.result.uuid)
          })
          .catch((e) => {
            this.errorMsg = e.response?.data.message || e.message
          })
    }
  }
}
</script>

<style scoped>

</style>
