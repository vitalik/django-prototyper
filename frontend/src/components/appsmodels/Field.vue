<template>
    <tr>
        <td>{{field.name}}</td>
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

