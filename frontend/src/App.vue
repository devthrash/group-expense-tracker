<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div class="container">
    <div class="box">
      <div class="buttons is-grouped">
          <router-link class="button" to="/">My groups</router-link>
          <router-link class="button" to="/new-group">New group</router-link>
        <router-link class="button" to="/logout">Log out</router-link>
      </div>

      <RouterView />
    </div>
  </div>
</template>

<style scoped>

</style>
