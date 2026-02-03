{{- define "mlops-streamlit-ui.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "mlops-streamlit-ui.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s" (include "mlops-streamlit-ui.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
