<template>
  <div class="box" v-for="group in groups">
    <h2 class="subtitle">{{ group.name }}</h2>

    <div class="tags">
      <span class="tag">{{ group.members.length }} members</span>
      <span class="tag">{{ group.expenses.length }} expenses</span>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" @click="viewGroup(group.uuid)">View</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "../utils/http";

export default {
  name: "MyGroups",

  data() {
    return {
      groups: []
    }
  },

  created() {
    axios.get('api/groups').then((response) => this.groups = response.data.results.groups)
  },

  methods: {
    viewGroup(id) {
      this.$router.push({
        name: 'view-group',
        params: {
          id
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
