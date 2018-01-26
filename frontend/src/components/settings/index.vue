<template>
    <div class="settings">
        <h2>Django Settings</h2>
        <hr>
        <table>

            <tr>
                <th>USE_I18N = </th>
                <td> <InputTrueFalse v-model.boolean="settings.USE_I18N" class="form-control" /></td>
            </tr>
            <tr>
                <th>USE_L10N = </th>
                <td> <InputTrueFalse v-model.boolean="settings.USE_L10N" class="form-control" /></td>
            </tr>
            <tr>
                <th>EMAIL_SUBJECT_PREFIX = </th>
                <td> <input v-model.lazy="settings.EMAIL_SUBJECT_PREFIX" class="form-control"></td>
            </tr>
            <tr>
                <th>ADMIN_SITE_HEADER = </th>
                <td> <input v-model.lazy="settings.ADMIN_SITE_HEADER" class="form-control"></td>
            </tr>
            <tr>
                <th>DEFAULT_FROM_EMAIL = </th>
                <td> <input v-model.lazy="settings.DEFAULT_FROM_EMAIL" class="form-control"></td>
            </tr>
            <tr>
                <th>TIME_ZONE = </th>
                <td> <input v-model.lazy="settings.TIME_ZONE" class="form-control"></td>
            </tr>
            <tr>
                <th>LANGUAGE_CODE = </th>
                <td> <input v-model.lazy="settings.LANGUAGE_CODE" class="form-control"></td>
            </tr>
        </table>
        

    </div>
</template>

<script>
import { store } from '../../store'
import InputTrueFalse from '../utils/InputTrueFalse'

export default {
    name: 'settings',
    data() {
        return {
            settings: store.project.settings
        }
    },
    components: {
        InputTrueFalse,
    }
}
</script>

<style lang="scss">

.settings {
    table th {
        font-weight: normal;
        text-align: right;
        padding-right: 4px;
    }
}

</style>
