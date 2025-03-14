provider "google" {
  project = "tjts5901-452510" 
  region  = "eu-west1"
}

# Enable Cloud Monitoring
resource "google_monitoring_notification_channel" "email1" {
  display_name = "Email Alerts"
  type         = "email"
  labels = {
    email_address = "ptjtammi@student.jyu.fi"  
  }
}


resource "google_monitoring_notification_channel" "email2" {
  display_name = "Email Alerts"
  type         = "email"
  labels = {
    email_address = "kaisa.m.jaaskelainen@student.savonia.fi"  
  }
}


resource "google_monitoring_notification_channel" "email3" {
  display_name = "Email Alerts"
  type         = "email"
  labels = {
    email_address = "otto.j.loukkalahti@student.jyu.fi"  
  }
}


# Create an Alert for High CPU Usage in GKE
resource "google_monitoring_alert_policy" "high_cpu_alert" {
  display_name = "GKE Flask App High CPU Alert"

  conditions {
    display_name = "High CPU Usage"
    condition_threshold {
      filter          = "metric.type=\"kubernetes.io/container/cpu/core_usage_time\" AND resource.type=\"k8s_container\""
      comparison      = "COMPARISON_GT"
      threshold_value = 0.8  # Alert if CPU usage > 80%
      duration        = "60s"
      aggregations {
        alignment_period   = "60s"
        per_series_aligner = "ALIGN_RATE"
      }
    }
  }

  combiner             = "OR"
  notification_channels = [google_monitoring_notification_channel.email1.id,
                           google_monitoring_notification_channel.email2.id,
                           google_monitoring_notification_channel.email3.id]

  documentation {
    content = "High CPU usage detected on Flask container in GKE."
  }
}