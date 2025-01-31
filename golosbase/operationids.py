op_names = [
    "vote",
    "comment",
    "transfer",
    "transfer_to_vesting",
    "withdraw_vesting",
    "limit_order_create",
    "limit_order_cancel",
    "feed_publish",
    "convert",
    "account_create",
    "account_update",
    "witness_update",
    "account_witness_vote",
    "account_witness_proxy",
    "pow",
    "custom",
    "report_over_production",
    "delete_comment",
    "custom_json",
    "comment_options",
    "set_withdraw_vesting_route",
    "limit_order_create2",
    "challenge_authority",
    "prove_authority",
    "request_account_recovery",
    "recover_account",
    "change_recovery_account",
    "escrow_transfer",
    "escrow_dispute",
    "escrow_release",
    "pow2",
    "escrow_approve",
    "transfer_to_savings",
    "transfer_from_savings",
    "cancel_transfer_from_savings",
    "custom_binary",
    "decline_voting_rights",
    "reset_account",
    "set_reset_account",
    "delegate_vesting_shares",
    "account_create_with_delegation",
    "account_metadata",
    "proposal_create",
    "proposal_update",
    "proposal_delete",
    "chain_properties_update",
    "break_free_referral",
    "delegate_vesting_shares_with_interest",
    "reject_vesting_shares_delegation",
    "transit_to_cyberway",
    "worker_request",
    "worker_request_delete",
    "worker_request_vote",
    "claim",
    "donate",
    "transfer_to_tip",
    "transfer_from_tip",
    "invite",
    "invite_claim",
    "account_create_with_invite",
    "asset_create",
    "asset_update",
    "asset_issue",
    "asset_transfer",
    "override_transfer",
    "invite_donate",
    "invite_transfer",
    "limit_order_cancel_ex",

    "fill_convert_request",
    "author_reward",
    "curation_reward",
    "comment_reward",
    "liquidity_reward",
    "interest",
    "fill_vesting_withdraw",
    "fill_order",
    "shutdown_witness",
    "fill_transfer_from_savings",
    "hardfork",
    "comment_payout_update",
    "comment_benefactor_reward",
    "return_vesting_delegation",
    "producer_reward",
    "delegation_reward",
    "auction_window_reward",
    "total_comment_reward",
    "worker_reward",
    "worker_state",
    "convert_sbd_debt",
    "internal_transfer",
    "comment_feed",
    "account_reputation",
    "minus_reputation",
    "comment_reply",
    "comment_mention",
    "accumulative_remainder",
    "authority_updated"
]

#: assign operation ids
operations = dict(zip(op_names, range(len(op_names))))
