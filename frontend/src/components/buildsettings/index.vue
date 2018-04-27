<template>
    <div>
        <div class="heading">
            <div class="container-fluid">
                <h2>Build Settings</h2>
            </div>
        </div>
        <div class="container-fluid">
            <table class="table table-sm" style="max-width: 660px;">
                <tr>
                    <td class="border-top-0">Translate in code</td>
                    <td class="border-top-0"><InputTrueFalse v-model.boolean="build_settings.ugettext_lazy" option_true="Yes" option_false="No" class="form-control form-control-sm" /></td>
                    <td class="border-top-0 w-50 text-muted">use ugettext_lazy <code>_('abc')</code> for text chunks in code</td>
                </tr>
                <!--
                <tr>
                    <td>PEP8 models.py</td>
                    <td><InputTrueFalse v-model.boolean="build_settings.pep8model_fields" option_true="Yes" option_false="No" class="form-control form-control-sm" /></td>
                    <td>for model fields try to wrap them to pass pep8</td>
                </tr>
                -->
                <tr>
                    <td>CharField max_lenght</td>
                    <td><input v-model.number="build_settings.charfield_max_length" type="number" style="max-width: 60px;"></td>
                    <td class="text-muted">default <code>max_lenght</code> value for all <code>CharField</code>s</td>
                </tr>
            </table>
        </div>
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
