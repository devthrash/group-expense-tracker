<template>

</template>

<script>
export default {
  name: "TheLogOut",

  created() {
    localStorage.clear()

    this.$router.push('/login')
  }
}
</script>

<style scoped>

</style>
