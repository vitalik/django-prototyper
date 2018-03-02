<template>
    <div>
        <h2>Build Settings</h2>
        <hr>

        <table class="table table-sm" style="max-width: 500px;">
            <tr>
                <td class="border-top-0">use ugettext_lazy <code>_('abc')</code> in code</td>
                <td class="border-top-0"><InputTrueFalse v-model.boolean="build_settings.ugettext_lazy" option_true="Yes" option_false="No" class="form-control form-control-sm" /></td>
            </tr>
            <tr>
                <td>for model fields try to wrap them to pass pep8</td>
                <td><InputTrueFalse v-model.boolean="build_settings.pep8model_fields" option_true="Yes" option_false="No" class="form-control form-control-sm" /></td>
            </tr>
            <tr>
                <td>default <code>max_lenght</code> for all <code>CharField</code>s</td>
                <td><input v-model.number="build_settings.charfield_max_length" type="number" style="max-width: 60px;"></td>
            </tr>
        </table>
    </div>
</template>

<script>
import { store } from '../../store'
import InputTrueFalse from '../utils/InputTrueFalse'

export default {
    name: 'buildsettings',
    data() {
        return {
            build_settings: store.project.build_settings
        }
    },
    mounted() {
        this._set_default('ugettext_lazy', true)
        this._set_default('pep8model_fields', false)
        this._set_default('charfield_max_length', 200)
    },
    methods: {
        _set_default(attr, value) {
            if (this.build_settings[attr] === undefined)
                this.$set(this.build_settings, attr, value)
        }
    },
    components: {
        InputTrueFalse,
    }
}

</script>
