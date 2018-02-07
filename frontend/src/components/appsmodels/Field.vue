<template>
    <tr class="field">
        <td>
            <input class="name" v-model.lazy="field.name">
        </td>
        <td>{{field.type}}</td>
    </tr>
</template>

<script>

export default {
    name: 'field',
    props: {
        field: {
            required: true,
            type: Object
        }
    }
}
</script>

<style scoped>
    .name {
        border: none;
        background: transparent;
    }
    tr.field td {
        border: none;
    }
</style>


