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

#Create alert for high memory usage
resource "google_monitoring_alert_policy" "high_memory_alert" {
  display_name = "GKE Flask App High Memory Alert"

  conditions {
    display_name = "High Memory Usage"
    condition_threshold {
      filter          = "metric.type=\"kubernetes.io/container/memory/used_bytes\" AND resource.type=\"k8s_container\""
      comparison      = "COMPARISON_GT"
      threshold_value = 0.8  # Alert if memory usage > 80%
      duration        = "60s"
      aggregations {
        alignment_period   = "60s"
        per_series_aligner = "ALIGN_SUM"
      }
    }
  }

  combiner             = "OR"
  notification_channels = [google_monitoring_notification_channel.email1.id,
                           google_monitoring_notification_channel.email2.id,
                           google_monitoring_notification_channel.email3.id]

  documentation {
    content = "High memory usage detected on Flask container in GKE."
  }
}

# Create an Alert for High Disk Usage
resource "google_monitoring_alert_policy" "high_node_disk_alert" {
  display_name = "GKE Flask App High Disk Usage Alert"

  conditions {
    display_name = "High Disk Usage"
    condition_threshold {
      filter          = "metric.type=\"compute.googleapis.com/instance/disk/read_bytes_count\" AND resource.type=\"gce_instance\""
      comparison      = "COMPARISON_GT"
      threshold_value = 10000000  
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
    content = "High disk usage detected on Flask container in GKE."
  }
}

resource "google_compute_network" "flask_network" {
  name = "flask-network"
}

resource "google_compute_firewall" "flask_allow_https" {
  name    = "flask-allow-https"
  network = google_compute_network.flask_network.id
  allow {
    protocol = "tcp"
    ports    = ["443"]
  }
  source_ranges = ["0.0.0.0/0"]
}