<template>
  <h1 class="title">{{ group.name }}</h1>

  <h2 class="subtitle">Members</h2>
  <table class="table">
    <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Role</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="member in group.members">
      <td>{{ member.name }}</td>
      <td>{{ member.email }}</td>
      <td>{{ member.email === group.created_by ? 'Creator' : 'Member' }}</td>
    </tr>
    </tbody>
  </table>

  <h2 class="subtitle">Expenses</h2>
  <table class="table">
    <thead>
    <tr>
      <th>Name</th>
      <th>Total</th>
      <th>Per member</th>
      <th colspan="2">Checked out</th>
    </tr>
    </thead>
    <tbody>
      <tr v-for="(expense, index) in group.expenses">
        <td>{{ expense.name }}</td>
        <td>{{ expense.cost }}</td>
        <td>{{ (expense.cost / group.members.length).toFixed(2) }}</td>
        <td :colspan="expense.checked_out ? 2 : 1">{{ expense.checked_out ? 'Yes' : 'No'}}</td>
        <td v-if="!expense.checked_out"><div class="button is-small" @click="checkout(expense.uuid, index)">Checkout</div></td>
      </tr>
    </tbody>
  </table>

  <h2 class="subtitle">Add new expense</h2>
  <form>
    <div class="field">
      <label class="label">Name</label>
      <div class="control">
        <input class="input" type="text" placeholder="Name" v-model="expense.name">
      </div>
    </div>
    <div class="field">
      <label class="label">Cost</label>
      <div class="control">
        <input class="input" type="number" placeholder="Cost" v-model="expense.cost">
      </div>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" @click="addExpense">Add</button>
      </div>
    </div>
  </form>
</template>

<script>
import axios from "../utils/http";

export default {
  name: "TheGroup",

  data() {
    return {
      group: {},
      expense: {
        name: '',
        cost: ''
      }
    }
  },

  created() {
    this.$watch(
        () => this.$route.params,
        (toParams, previousParams) => {
          if (toParams.id !== previousParams.id) {
            this.getGroup(toParams.id)
          }
        }
    )

    this.getGroup(this.$route.params.id)
  },

  methods: {
    getGroup(id) {
      axios.get('api/groups/' + id)
          .then((response) => {
            this.group = response.data.result
          })
    },

    addExpense(e) {
      e.preventDefault()

      const config = {
        method: 'post',
        url: 'api/expenses/',
        data: {
          ...this.expense,
          group: this.group.name
        }
      }

      axios(config)
          .then(() => {
            location.reload()
          })
    },

    checkout(uuid, index) {
      const config = {
        method: 'post',
        url: 'api/checkout/' + uuid,
        data: {
          checked_out: true
        }
      }

      axios(config).then(() => {
        this.group.expenses[index].checked_out = true
      })
    }
  }
}
</script>

<style scoped>

</style>
