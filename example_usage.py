from client import EventDrivenOmnichannelLifecycleNudgeDispatcherClient

def main():
    client = EventDrivenOmnichannelLifecycleNudgeDispatcherClient()
    res = client.dispatch_lifecycle_nudge('SUBSCRIPTION_CHURN_RISK_INACTIVE_14D', 'user@tech.io', 20)
    print('Lifecycle Nudge Dispatcher: ' + res['nudge_dispatch_id'] + ' (' + res['trigger'] + ')')
    print('Channels: ' + ', '.join(res['channels_dispatched']) + ' | Latency: ' + str(res['delivery_latency_ms']) + 'ms')
    print('Projected Recovery Rate: ' + str(res['projected_recovery_conversion_rate_pct']) + '%')
    print('Workflow: ' + res['lifecycle_workflow_graph_url'])

if __name__ == '__main__':
    main()
