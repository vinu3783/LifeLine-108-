from twilio.rest import Client
from flask import current_app as app

class SMSService:
    def __init__(self):
        pass

    def _get_client(self):
        sid = app.config.get('TWILIO_ACCOUNT_SID', '')
        token = app.config.get('TWILIO_AUTH_TOKEN', '')
        if not sid or not token:
            return None
        return Client(sid, token)

    @property
    def twilio_phone(self):
        return app.config.get('TWILIO_PHONE_NUMBER', '')
    
    def send_location_share_link(self, to_phone, location_link):
        """Send location sharing link to the victim"""
        message = (
            f"Emergency Response: Please click on this link to share your exact location: "
            f"{location_link}"
        )
        return self._send_sms(to_phone, message)
    
    def notify_ambulance_driver(self, driver_phone, victim_lat, victim_lon, address, route_url):
        """Notify ambulance driver about the emergency"""
        message = (
            f"EMERGENCY ALERT: You have been assigned to an emergency at: {address}. "
            f"Location coordinates: {victim_lat}, {victim_lon}. "
            f"Route: {route_url}"
        )
        return self._send_sms(driver_phone, message)
    
    def send_confirmation_to_victim(self, victim_phone, ambulance_id, driver_name, eta_minutes):
        """Send confirmation to the victim that ambulance is on the way"""
        message = (
            f"Emergency Response: Ambulance {ambulance_id} has been dispatched to your location. "
            f"Driver: {driver_name}. Estimated arrival time: {eta_minutes} minutes. "
            f"Stay calm and wait for help to arrive."
        )
        return self._send_sms(victim_phone, message)
    
    def _send_sms(self, to_phone, message):
        """Private method to send SMS using Twilio"""
        client = self._get_client()
        if not client:
            app.logger.warning("Twilio not configured — SMS skipped.")
            return {"success": False, "error": "Twilio not configured"}
        try:
            if not to_phone.startswith('+'):
                to_phone = '+' + to_phone
            msg = client.messages.create(
                body=message,
                from_=self.twilio_phone,
                to=to_phone
            )
            return {"success": True, "message_sid": msg.sid}
        except Exception as e:
            app.logger.error(f"Error sending SMS: {str(e)}")
            return {"success": False, "error": str(e)}
        

        # Add this method to the SMSService class
def send_location_share_link(self, to_phone, location_share_url):
    """Send location sharing link to the victim"""
    message = (
        f"Emergency Response: Please click on this link to share your exact location: "
        f"{location_share_url}"
    )
    return self._send_sms(to_phone, message)